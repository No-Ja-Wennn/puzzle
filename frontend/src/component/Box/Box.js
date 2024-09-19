import classNames from "classnames/bind"
import styles from "./Box.module.scss"

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBoltLightning } from '@fortawesome/free-solid-svg-icons';

const cx = classNames.bind(styles)

function Box() {
    return <div className={cx('wrapper')} >
        <span className={cx('text')}>Xin chào</span>
    </div>;
}

export default Box;