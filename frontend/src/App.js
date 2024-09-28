import logo from './logo.svg';
import './App.css';
import Box from './component/Box/Box';
import Text from './component/Text/Text';
import Wrapper from './component/Wrapper';
import { useState } from 'react';

function App() {
  const [values, setValues] = useState([[1, 2, 3], [1, 2, 3], [1, 2, 3]]);

  return (
    <div className="App">
      <Wrapper>
        {values.map((row, rowIndex) => (
          <div key={rowIndex} className="row">
            {row.map((col, colIndex) => (
              <Box key={colIndex}>{col}</Box>
            ))}
          </div>
        ))}
      </Wrapper>
    </div>
  );
}

export default App;
