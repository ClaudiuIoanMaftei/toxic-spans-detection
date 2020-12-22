import React, {useEffect, useState} from "react";

import Button from "../Button";
import ResizebleTextarea from "../ResizebleTextArea";

import "./_index.scss";

type HomeProps = {
    connection?: WebSocket;
    message?: any;
}

enum STEP {
    PREPROCESSING = "PREPROCESSING",
    ANALYZING = "ANALYZING",
    POSTPROCESSING = "POSTPROCESSING"
}

const Home: React.FunctionComponent<HomeProps> = (props) => {
    const [text, setText] = useState<string>();
    const [finishedSteps, setFinishedSteps] = useState<STEP[]>([]);
    const [isLoading, setIsLoading] = useState(false);
    const [spans, setSpans] = useState<number[]>();

    useEffect(() => {

        if (props.message) {

            if (props.message.includes(STEP.PREPROCESSING)) {
                setFinishedSteps([...finishedSteps, STEP.PREPROCESSING])
            } else if (props.message.includes(STEP.ANALYZING)) {
                setFinishedSteps([...finishedSteps, STEP.ANALYZING])
            } else if (props.message.includes(STEP.POSTPROCESSING)) {
                setFinishedSteps([...finishedSteps, STEP.POSTPROCESSING])
                setIsLoading(false);
            } else {
                const plainSpans = props.message;
                setSpans(plainSpans.replace("[", "").replace("]", "").split(",").map((el: string) => (+el)));
            }
        }

    }, [props.message])

    const handleOnChange = (value: string) => {
        setText(value);
    }

    const handleOnCheck = () => {
        props.connection && props.connection.send(text ?? '');
        setIsLoading(true);
    }

    return <div className="main--container">
        <ResizebleTextarea className="main--container__input" onChange={handleOnChange} spans={spans}/>
        <div className="main--container__results">
            <Button className="analyze" isLoading={isLoading} onClick={handleOnCheck}> Analyze text </Button>
            <ul>
                {finishedSteps.map((step) => (
                    <li key={step}><p className="has-text-weight-bold is-capitalized is-italic">{step as STEP}...</p>
                    </li>))}
            </ul>
        </div>
    </div>;
}

export default Home;