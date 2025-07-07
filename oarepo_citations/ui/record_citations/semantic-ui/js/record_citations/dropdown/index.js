import React from "react";
import ReactDOM from "react-dom";

import { RecordCitations } from "./components";

const recordCitationsAppDiv = document.getElementById("record-citations");
const settings = JSON.parse(recordCitationsAppDiv.dataset.citationSettings);

ReactDOM.render(
  <RecordCitations
    record={JSON.parse(recordCitationsAppDiv.dataset.record)}
    citationStyles={settings?.styles}
    defaultStyle={settings?.defaultStyle ?? "iso690-author-date-cs"}
  />,
  recordCitationsAppDiv
);


export { RecordCitations as RecordCitationsDropdown };
