function Answer({ data }) {
  if (!data) return null;

  const notFound =
    data.answer?.toLowerCase().includes(
      "couldn't find that information"
    );

  return (
    <div className="card answer-card">
      <h2>Answer</h2>

      <p className="answer-text">
        {data.answer}
      </p>

      {!notFound && data.sources?.length > 0 && (
        <>
          <h3>Sources</h3>

          <div className="sources">
            {data.sources.map((source, index) => (
              <div className="source" key={index}>
                📄 {source.document} — Page {source.page}
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default Answer;