import React from "react";
import PropTypes from "prop-types";

import { i18next } from "@translations/oarepo_citations";

import { List, Message } from "semantic-ui-react";

import { useCitation } from "../../hooks";
import { PlaceholderLoader } from "../../components";
import { ClipboardCopyButton } from "@js/oarepo_ui/components";

const CitationListItem = ({ recordLink, style, label }) => {
  const effectiveLabel = label ?? i18next.t(style);

  const { citation, loading, error } = useCitation(recordLink, style);

  const ErrorMessage = ({ message }) => {
    return <Message negative role="status" aria-label={i18next.t(`Error generating ${effectiveLabel} citation`)}>{message}</Message>;
  };

  return (
    <List.Item>
      {!error &&
        <List.Content floated="right">
          <ClipboardCopyButton copyText={citation} className="ui button copy outline link icon copy-button" />
        </List.Content>
      }
      <List.Content as="article">
        <List.Header as="h3">{effectiveLabel}</List.Header>
        <List.Description>
          {(loading && <PlaceholderLoader />) || citation}
          {error && <ErrorMessage message={error} />}
        </List.Description>
      </List.Content>
    </List.Item>
  );
};

CitationListItem.propTypes = {
  recordLink: PropTypes.string.isRequired,
  style: PropTypes.string.isRequired,
  label: PropTypes.string,
};

export default CitationListItem;
