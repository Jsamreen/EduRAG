import { useState } from "react";
import api from "../../api/api";

function Upload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadDocument = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      await api.post("/documents/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert("✅ Document uploaded and indexed successfully!");

      if (onUploadSuccess) {
        onUploadSuccess(file.name);
      }

      setFile(null);

    } catch (err) {
      console.error(err);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">

      <h2>Upload University PDF</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={uploadDocument}
        disabled={loading}
      >
        {loading ? "Uploading..." : "Upload"}
      </button>

    </div>
  );
}

export default Upload;