import { useState } from "react";
import api from "../api/api";
import Message from "./Message";

function ChatBox() {

    const [messages, setMessages] = useState([]);

    const [question, setQuestion] = useState("");

    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {

        if (question.trim() === "")
            return;

        const userMessage = {

            text: question,

            user: true

        };

        setMessages(prev => [...prev, userMessage]);

        setLoading(true);

        try {

            const res = await api.post(

                "/chat/chat",

                {

                    question

                }

            );

            setMessages(prev => [

                ...prev,

                {

                    text: res.data.answer,

                    user: false

                }

            ]);

        }

        catch (err) {

            console.log(err);

            console.log("Status:", err.response?.status);

            console.log("Data:", err.response?.data);

            alert(JSON.stringify(err.response?.data));

        }

        setQuestion("");

        setLoading(false);

    };

    return (

        <div className="chat-area">

            <div className="messages">

                {

                    messages.map(

                        (m, i) =>

                            <Message

                                key={i}

                                text={m.text}

                                isUser={m.user}

                            />

                    )

                }

                {

                    loading &&

                    <Message

                        text="Thinking..."

                        isUser={false}

                    />

                }

            </div>

            <div className="input-area">

                <input

                    value={question}

                    onChange={(e) => setQuestion(e.target.value)}

                    onKeyDown={(e) => {

                        if (e.key === "Enter") {

                            sendMessage();

                        }

                    }}

                    placeholder="Ask anything..."

                />

                <button onClick={sendMessage}>

                    Send

                </button>

            </div>

        </div>

    );

}

export default ChatBox;