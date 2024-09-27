import classNames from "classnames/bind";
import styles from "./Hello.module.scss"

const cx = classNames.bind(styles);

function Hello() {
    return <div className={cx("wrapper")}>hello</div>;
}

export default Hello;