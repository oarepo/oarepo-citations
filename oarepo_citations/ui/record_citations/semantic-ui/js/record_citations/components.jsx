import React, { memo } from "react";
import { Placeholder } from "semantic-ui-react";

import { decode } from "html-entities";
import sanitizeHtml from "sanitize-html";
import Linkify from "linkify-react";

export const PlaceholderLoader = () => {
  return (
    <Placeholder fluid role="presentation">
      <Placeholder.Paragraph>
        <Placeholder.Line />
        <Placeholder.Line />
        <Placeholder.Line />
      </Placeholder.Paragraph>
    </Placeholder>
  );
};

export const LinkifiedCitation = memo(({ citation }) => {
  const decodedCitation = decode(citation);
  const sanitizedCitation = sanitizeHtml(decodedCitation, {
    allowedTags: ["a", "b", "i", "em", "strong", "p"],
    allowedAttributes: {
      a: ["href", "target", "rel"],
    },
  });

  return (
    <Linkify 
      as="div" 
      options={{ target: "_blank", rel: "noopener noreferrer", className: "word-break-all" }}
    >
      {sanitizedCitation}
    </Linkify>
  );
});
