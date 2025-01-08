import React from "react";
import PropTypes from "prop-types";

import { i18next } from "@translations/i18next";

const ClipboardCopyButton = ({ copyText }) => {
  return (
    <i
      title={`${i18next.t("Click to copy")}: ${copyText}`}
      role="button"
      className="copy outline link teal icon copy-btn rel-ml-1"
      data-clipboard-text={copyText}
    />
  );
};

ClipboardCopyButton.propTypes = {
  copyText: PropTypes.string.isRequired,
};

export default ClipboardCopyButton;
