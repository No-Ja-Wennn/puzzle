import classNames from "classnames/bind";
import styles from "./Box.module.scss";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  fa0,
  faBoltLightning,
  faCarSide,
  faXmark,
} from "@fortawesome/free-solid-svg-icons";
import { useEffect, useRef } from "react";

const cx = classNames.bind(styles);

function Box({
  type,
  value,
  active,
  rowIndex,
  colIndex,
  setvalue,
  activeIndex,
  onClick = () => {},
}) {
  const inputRef = useRef();

  useEffect(() => {
    // console.log(activeIndex)
    if (activeIndex && activeIndex.col === colIndex && activeIndex.row === rowIndex)
      inputRef.current.focus();
  }, [activeIndex]);

  const handleChange = (e) => {
    const inputValue = e.target.value;
    if (inputValue === "")
      setvalue((prev) => {
        const new_prev = [...prev];
        new_prev[rowIndex][colIndex] = "";
        return new_prev;
      });
    else if (
      inputValue.length === 1 &&
      !isNaN(inputValue) &&
      inputValue >= "1" &&
      inputValue <= "8"
    ) {
      setvalue((prev) => {
        const new_prev = [...prev];
        let flag = true;
        new_prev.forEach((row) =>
          row.forEach((col) => {
            if (col === parseInt(inputValue)) flag = false;
          })
        );
        if (flag) new_prev[rowIndex][colIndex] = parseInt(inputValue);
        return new_prev;
      });
    }
  };
  return (
    <div className={cx("wrapper", { active })} onClick={onClick}>
      {/* <FontAwesomeIcon icon={faXmark}></FontAwesomeIcon> */}
      {type === "input" ? (
        <input
          ref={inputRef}
          className={cx("input")}
          value={value}
          onChange={handleChange}
        />
      ) : (
        <span className={cx("text")}>{value}</span>
      )}
    </div>
  );
}

export default Box;
