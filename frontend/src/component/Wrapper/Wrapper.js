import React, { useRef, useEffect } from 'react';
import classNames from 'classnames/bind';
import styles from './Wrapper.module.scss';

const cx = classNames.bind(styles);

export function Wrapper({ children }) {
    const wrapperRef = useRef(null);

    useEffect(() => {
        const handleResize = () => {
            if (wrapperRef.current) {
                const width = wrapperRef.current.offsetWidth;
                document.documentElement.style.setProperty('--current-width', `${width}px`);
            }
        };

        handleResize();
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    return (
        <div ref={wrapperRef} className={cx("puzzle")}>
            {children}
        </div>
    );
}

export default Wrapper;
