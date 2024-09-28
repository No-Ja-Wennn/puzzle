import classNames from "classnames/bind"
import styles from "./Box.module.scss"

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { fa0, faBoltLightning, faCarSide, faXmark } from '@fortawesome/free-solid-svg-icons';

const cx = classNames.bind(styles)

function Box() {
    return (
        <div className={cx("wrapper")}> 
            {/* <FontAwesomeIcon icon={faXmark}></FontAwesomeIcon> */}
        </div>
    );
}

export default Box;