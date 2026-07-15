import logging
from pathlib import Path

import pymupdf
from fastapi import HTTPException, status

from app.schemas.document import ExtractedPage

logger = logging.getLogger(__name__)


class PDFExtractionService:
    """Extract page-level text and metadata from PDF documents."""

    def extract_text(self, pdf_path: Path) -> dict[str, object]:
        """Extract text from a PDF while preserving page numbers."""

        if not pdf_path.exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The requested PDF document was not found.",
            )

        pages: list[ExtractedPage] = []

        try:
            with pymupdf.open(pdf_path) as document:
                if document.page_count == 0:
                    raise HTTPException(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail="The uploaded PDF does not contain any pages.",
                    )

                for page_index, page in enumerate(document):
                    raw_text = page.get_text("text")
                    cleaned_text = self._clean_text(raw_text)

                    pages.append(
                        ExtractedPage(
                            page_number=page_index + 1,
                            text=cleaned_text,
                            character_count=len(cleaned_text),
                        )
                    )

                pages_with_text = sum(
                    1 for page in pages if page.text.strip()
                )

                total_characters = sum(
                    page.character_count for page in pages
                )

                logger.info(
                    "Extracted %s characters from %s pages in '%s'",
                    total_characters,
                    document.page_count,
                    pdf_path.name,
                )

                return {
                    "total_pages": document.page_count,
                    "pages_with_text": pages_with_text,
                    "total_characters": total_characters,
                    "pages": pages,
                }

        except HTTPException:
            raise

        except pymupdf.FileDataError as exc:
            logger.exception(
                "Invalid or damaged PDF: %s",
                pdf_path,
            )

            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="The uploaded file is not a valid readable PDF.",
            ) from exc

        except Exception as exc:
            logger.exception(
                "Unexpected error while extracting PDF text: %s",
                pdf_path,
            )

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Text could not be extracted from the PDF.",
            ) from exc

    @staticmethod
    def _clean_text(text: str) -> str:
        """Apply basic cleanup without changing document meaning."""

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        return "\n".join(lines)


pdf_extraction_service = PDFExtractionService()