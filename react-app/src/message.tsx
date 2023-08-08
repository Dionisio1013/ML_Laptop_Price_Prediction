// Function based components are recommended for conciseness

// PascalCasing - Capitalize the first letter of a word
function Message(){
    // JSX: Javascript XML
    const name = 'Mosh'
    
    // the name below here is an expression
    // expression is a piece of code that produces a value
    // Can refer to a variable or a funciton 
    return <h1>Hello {name}</h1>;
}

export default Message;