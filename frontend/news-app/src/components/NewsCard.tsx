type news = {
  title: string;
  description: string;
  date: string;
  category: string;
};

interface newsCardProps {
  newsSets: news[];
}
function NewsCard({ newsSets }: newsCardProps) {
  return (
    <div className="news-card-container">
      {newsSets.map((newsSet, index) => (
        <div key={index} className="news-card">
          <h3 className="news-card-title">{newsSet.title}</h3>
          <p className="news-card-description">{newsSet.description}</p>
          <p className="news-card-date">{newsSet.date}</p>
          <p className="news-card-catefory">{newsSet.category}</p>
        </div>
      ))}
    </div>
  );
}

export default NewsCard;
