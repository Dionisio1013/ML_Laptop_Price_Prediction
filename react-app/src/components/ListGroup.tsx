interface Props {
  items: string[];
  heading: string;
  // (item: string) => void
  onSelectItem: (item: string) => void; // onClick
}

import { useState } from "react";

function ListGroup({ items, heading, onSelectItem }: Props) {
  // Hook - a function that allows us to tap into built in features in React
  const [selectedIndex, setSelectedIndex] = useState(-1);
  // const [name, setName] = useState("");

  // Can only use html elements and react js
  // HOWEVER if we use and expression {}, we can implement if statements and stuff like that

  return (
    // Have to put our files in <> to have mupltiple different types of tags
    <>
      <h1>Graphics Quality</h1>
      {items.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          // Whenever this action is committed. Calling the function
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
