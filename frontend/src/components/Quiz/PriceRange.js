import '../../App.css';
import React, { useState, useEffect } from "react";
import Slider from 'react-slider';

const MIN = 0;
const MAX = 100;

export default function PriceRange({ formData, setValues}) {
    const [priceRange, setPriceRange] = useState([MIN, MAX]);

    useEffect(() => {
        try {
            const parsedPriceRange = JSON.parse(formData.priceRange);
            setPriceRange(parsedPriceRange);
        } catch (error) {
            console.error('Failed to parse formData.priceRange:', error);
        }
    }, [formData.priceRange]);

    return (
        <div className="priceRange">
            <div className="box" id="priceRange">
                <h3>Price <span>Range</span></h3>
                <div className={"values"}>€{priceRange[0]} - €{priceRange[1]}</div>
                <small>
                    Current range: €{priceRange[1] - priceRange[0]}
                </small>

                <Slider className={"slider"}
                    onChange={(value) => {
                        setPriceRange(value);
                        setValues(value);
                    }}
                    value={priceRange}
                    min={MIN}
                    max={MAX} />
            </div>
        </div>
    );
}