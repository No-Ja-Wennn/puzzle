import classNames from "classnames/bind";
import styles from "./Text.module.scss";

const cx = classNames.bind(styles);

function Text() {
    return <div className={cx("hello")}>ok trai</div>
}

export default Text;