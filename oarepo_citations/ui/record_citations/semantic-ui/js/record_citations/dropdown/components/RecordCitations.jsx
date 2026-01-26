import React from "react";
import PropTypes from "prop-types";

import CitationField from "./CitationField";

export const RecordCitations = ({
  record,
  citationStyles = [
    { style: "iso690-author-date-cs", label: "ČSN ISO 690" },
    { style: "apa", label: "APA" },
    { style: "harvard-cite-them-right", label: "Harvard" },
    { style: "modern-language-association", label: "MLA" },
    { style: "vancouver", label: "Vancouver" },
    { style: "chicago-fullnote-bibliography", label: "Chicago" },
    { style: "ieee", label: "IEEE" },
    { style: "bibtex", label: "BibTeX" },
  ],
  defaultStyle = "iso690-author-date-cs",
}) => {
  return (
    <CitationField
      record={record}
      styles={citationStyles}
      defaultStyle={defaultStyle}
    />
  );
};

RecordCitations.propTypes = {
  record: PropTypes.object.isRequired,
  // eslint-disable-next-line react/require-default-props
  citationStyles: PropTypes.array,
  // eslint-disable-next-line react/require-default-props
  defaultStyle: PropTypes.string,
};
