import React from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';


const TextAnswer = styled.div`
  font-size: 14px;
`;

const TextAnswers = ({ answers }) => (
  <>
    {answers.map((answer) => (
      <TextAnswer key={answer.text}>{answer.text}</TextAnswer>
    ))}
  </>
);

export default TextAnswers;

TextAnswers.propTypes = {
  answers: PropTypes.array.isRequired,
};
