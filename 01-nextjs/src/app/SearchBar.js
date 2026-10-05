"use client";
import { useState } from "react";

export default function SearchBar() {
  var [typedText, setTypedText] = useState("");

  function whenStudentTypes(event) {
    var newText = event.target.value;
    setTypedText(newText);
  }

  return (
    <div>
      <input
        type="text"
        placeholder="Type a course name"
        value={typedText}
        onChange={whenStudentTypes}
      />
      <p>You typed: {typedText}</p>
    </div>
  );
}