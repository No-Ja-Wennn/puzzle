import "./App.css";
import Wrapper from "./component/Wrapper";
import { useEffect, useState } from "react";

function App() {
  const [valueStart, setValueStart] = useState([
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
  ]);
  const [valueEnd, setValueEnd] = useState([
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
  ]);

  const [response, setReponse] = useState([]);

  const [activeWrapper, setActiveWrapper] = useState(null);

  useEffect(() => {
    console.log(activeWrapper);
  }, [activeWrapper]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("send: ", {
      start: valueStart,
      goal: valueEnd,
    });

    fetch("http://127.0.0.1:8000/api/send/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        data: {
          start: valueStart,
          goal: valueEnd,
        },
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("result: ", result.result);
        result.result.shift()
        result.result.pop()
        setReponse(result.result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  const handleReset = () => { setReponse([]) };

  return (
    <div className="App">
      <h1>Puzzle</h1>
      <div className="show">
        <div className="box1">
          <Wrapper
            boxIndex={1}
            value={valueStart}
            setValue={setValueStart}
            activeWrapper={activeWrapper}
            setActiveWrapper={() => setActiveWrapper(1)}
          />
          {
            response.map((array, indexArray) => (
              <Wrapper
                key={indexArray}
                boxIndex={0}
                value={array}
                setValue={() => { }}
                activeWrapper={-1}
                setActiveWrapper={() => { }}
                type="text"
              />
            ))
          }
          <div className="wrapper">
            <button className="btn" onClick={handleSubmit}>
              Submit
            </button>
          </div>
        </div>
        <div className="box2">

          <Wrapper
            boxIndex={2}
            value={valueEnd}
            setValue={setValueEnd}
            activeWrapper={activeWrapper}
            setActiveWrapper={() => setActiveWrapper(2)}
          />
          <div className="wrapper">
            <button className="btn" onClick={handleReset}>
              Reset
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
