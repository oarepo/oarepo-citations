import React from "react";
import { Placeholder } from "semantic-ui-react";

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