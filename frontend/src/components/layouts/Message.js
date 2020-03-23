import React from 'react';

function Message(props) {
    let messageContent = '';

    if (props.sender === 'eckmo') {
        // Allow eckmo to respond with markdown
        messageContent = <div dangerouslySetInnerHTML={{ __html: props.content }} />;
    }
    else {
        messageContent = props.content;
    }

    return (
        <div className={`msg msg-${props.sender}`}>
            {messageContent}
        </div>
    )
}

export default Message;