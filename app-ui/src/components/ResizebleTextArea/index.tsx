import React, {FormEvent, useEffect, useState} from "react";


import "./_index.scss";

type ResizebleTextareaProps = {
    onChange?: any;
    className?: string;
    value?: string;
    spans?: number[];
}


const updateTextColors = (text: string, spans:number[]) => {
    // console.log("____");
    // console.log(text);
    const end = "</span>";
    const start = "<span style='color: red'>";

    let lastSpan = spans[spans.length - 1];

    for(let i=spans.length - 2; i>=0; i--){
        if((spans[i + 1] - spans[i]) > 1 || i == 0){
            console.log(spans[i + 1], lastSpan);

            text = [text.slice(0, lastSpan), end, text.slice(lastSpan)].join('');
            text = [text.slice(0, spans[i + 1] - 1), start, text.slice(spans[i + 1] - 1)].join('');

            lastSpan = spans[i];
        }
    }

    return text;
}

const ResizebleTextarea: React.FunctionComponent<ResizebleTextareaProps> = (props) => {
    const [value, setValue] = useState<string>("");

    useEffect(() => {
        let el = document.getElementById("textarea");
        if(el) el.innerHTML = updateTextColors(value, props.spans ?? []);
    }, [props.spans])

    const handleChange = (event: FormEvent<HTMLDivElement>) => {
        if(event.currentTarget && event.currentTarget.textContent) {
            props.onChange(event.currentTarget.textContent);
            setValue(event.currentTarget.textContent);
        }
    };

        return (
            <p
                contentEditable={true}
                id="textarea"
                placeholder={'Enter your text here...'}
                className={`text ${props.className ?? ""}`}
                onInput={handleChange}
            />
        )
}

export default ResizebleTextarea;