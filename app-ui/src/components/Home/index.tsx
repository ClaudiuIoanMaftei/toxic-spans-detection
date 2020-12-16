import React, {ChangeEvent, useState} from "react";

import Button from "../Button";

import "./_index.scss";

type HomeProps = {
    connection?: WebSocket;
}

const Home: React.FunctionComponent<HomeProps> = (props) => {
    const [text, setText] = useState<string>();


    const handleOnChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
        setText(event.target.value);
    }

    const handleOnCheck = () => {
        // props.connection && props.connection.send(text ?? '');
    }

    return <div className="main--container">
        <textarea className="main--container__input" onChange={handleOnChange}>

        </textarea>
        <div className="main--container__controls">
        <Button onClick={handleOnCheck}> Check </Button>
        </div>
        </div>;
}

export default Home;