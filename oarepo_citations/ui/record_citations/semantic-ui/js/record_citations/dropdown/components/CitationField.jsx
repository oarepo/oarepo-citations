import React from "react";
import PropTypes from "prop-types";

import { Dropdown, Message } from "semantic-ui-react";
import { i18next } from "@translations/invenio_app_rdm/i18next";
import _escape from "lodash/escape";

import { ClipboardCopyButton } from "@js/oarepo_ui/components";
import { useCitation } from "../../hooks";
import { PlaceholderLoader } from "../../components";

const CitationField = ({
  styles,
  record,
  defaultStyle,
}) => {
  const recordLink = record.links.self;

  const { getCitation, citation, loading, error } = useCitation(recordLink, defaultStyle);

  const ErrorMessage = ({ message }) => {
    return <Message negative role="status" aria-label={i18next.t("Error generating citation.")}>{message}</Message>;
  };

  const escapedCitation = _escape(citation);
  const urlRegex = /(https?:\/\/[^\s,;]+(?=[^\s,;]*))/g;
  const urlizedCitation = escapedCitation.replace(urlRegex, (url) => {
    let trailingDot = "";
    if (url.endsWith(".")) {
      trailingDot = ".";
      url = url.slice(0, -1);
    }
    return `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>${trailingDot}`;
  });

  const citationOptions = styles.map((style) => {
    return {
      key: style.style,
      value: style.style,
      text: style.label,
    };
  });

  const onFieldChange = (_, data) => {
    getCitation(data.value);
  };

  return (
    <div>
      {!error ?
        <div id="citation-text" className="wrap-overflowing-text rel-mb-1">
          {loading ? (
            <PlaceholderLoader />
          ) : (
            <div dangerouslySetInnerHTML={{ __html: urlizedCitation }} />
          )}
        </div> :
        <ErrorMessage message={error} />
      }
      <div className="auto-column-grid no-wrap">
        <div className="flex align-items-center">
          <label id="citation-style-label" className="mr-10">
            {i18next.t("Style")}
          </label>
          <Dropdown
            className="citation-dropdown rel-mr-1"
            aria-labelledby="citation-style-label"
            defaultValue={defaultStyle}
            options={citationOptions}
            fluid
            selection
            onChange={onFieldChange}
          />
          <ClipboardCopyButton copyText={citation} />
        </div>
      </div>
    </div>
  );
};

CitationField.propTypes = {
  styles: PropTypes.array.isRequired,
  record: PropTypes.object.isRequired,
  defaultStyle: PropTypes.string.isRequired,
};

export default CitationField;
