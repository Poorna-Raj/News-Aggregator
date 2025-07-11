import { useEffect, useState } from "react";
import NewsCard from "./components/NewsCard";

function App() {
  const API_URL = "http://127.0.0.1:8000/";
  const [news, setNews] = useState([]);
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) throw Error("Did not recive expected data");
        const result = await response.json();
        setNews(result);
      } catch (err) {
        console.log(err);
      }
    };
    setTimeout(() => {
      (async () => fetchItems())();
    }, 2000);
  }, []);
  return <NewsCard newsSets={news}></NewsCard>;
}

export default App;
