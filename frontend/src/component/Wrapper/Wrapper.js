import React, { useRef, useEffect, useState } from "react";
import classNames from "classnames/bind";
import styles from "./Wrapper.module.scss";
import Box from "../Box/Box";

const cx = classNames.bind(styles);

export function Wrapper({boxIndex, value, setValue, activeWrapper, setActiveWrapper }) {
  const wrapperRef = useRef(null);
//   useEffect(() => {
//     const handleResize = () => {
//       if (wrapperRef.current) {
//         const width = wrapperRef.current.offsetWidth;
//         document.documentElement.style.setProperty(
//           "--current-width",
//           `${width}px`
//         );
//       }
//     };

//     handleResize();
//     window.addEventListener("resize", handleResize);

//     return () => {
//       window.removeEventListener("resize", handleResize);
//     };
//   }, []);

  const [active, setActive] = useState({
    row: null,
    col: null,
  });

  const handleActive = (row, col) => {
    setActive({
      row: row,
      col: col,
    });
  };

  useEffect(() => {
    console.log(boxIndex , activeWrapper)
    const handleKeyLeft = (event) => {
      if (event.key === "ArrowLeft") {
        setActive((prev) => {
          const colIndex = prev.col;
          if (colIndex >= 1 && colIndex <= 2) {
            return { ...prev, col: colIndex - 1 };
          }
          return prev;
        });
      }
    };
    const handleKeyRight = (event) => {
      if (event.key === "ArrowRight") {
        setActive((prev) => {
          const colIndex = prev.col;
          if (colIndex >= 0 && colIndex <= 1) {
            return { ...prev, col: colIndex + 1 };
          }
          return prev;
        });
      }
    };
    const handleKeyTop = (event) => {
      if (event.key === "ArrowUp") {
        setActive((prev) => {
          const rowIndex = prev.row;
          if (rowIndex >= 1 && rowIndex <= 2) {
            return { ...prev, row: rowIndex - 1 };
          }
          return prev;
        });
      }
    };
    const handleKeyDown = (event) => {
      if (event.key === "ArrowDown") {
        setActive((prev) => {
          const rowIndex = prev.row;
          if (rowIndex >= 0 && rowIndex <= 1) {
            return { ...prev, row: rowIndex + 1 };
          }
          return prev;
        });
      }
    };
    if (boxIndex === activeWrapper){
        window.addEventListener("keydown", handleKeyLeft);
        window.addEventListener("keydown", handleKeyRight);
        window.addEventListener("keydown", handleKeyTop);
        window.addEventListener("keydown", handleKeyDown);
    }

    return () => {
      window.removeEventListener("keydown", handleKeyLeft);
      window.removeEventListener("keydown", handleKeyRight);
      window.removeEventListener("keydown", handleKeyTop);
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [activeWrapper]);

  return (
    <div ref={wrapperRef} className={cx("puzzle")} onClick={setActiveWrapper}>
      {value.map((row, rowIndex) =>
        row.map((col, colIndex) => (
          <Box
            key={colIndex}
            rowIndex={rowIndex}
            colIndex={colIndex}
            active={active.row === rowIndex && active.col === colIndex}
            type="input"
            value={col}
            activeIndex={active}
            setvalue={setValue}
            onClick={() => handleActive(rowIndex, colIndex)}
          />
        ))
      )}
    </div>
  );
}

export default Wrapper;
