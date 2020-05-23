import React from 'react';
import PropTypes from 'prop-types';
import emotion from 'emotion';
import styled from '@emotion/styled';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';


const AnswersContainer = styled.div`
  margin-top: 60px;
  margin-left: 60px;
`;

const AnswerContainer = styled.a`
  cursor: pointer;
  margin-top: 40px;
  display: flex;
  align-items: center;
`;

const TextAnswer = styled.span`
  font-size: 20px;
  margin-left: 20px;
`;

const IconContainer = styled.div`
  opacity: 0;

  &:hover {
    opacity: 1;
  }
`;


const TextAnswers = ({ answerOptions, onAnswerClick }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.text}
        onClick={() => onAnswerClick(answer)}
      >
        <IconContainer>
          <Leaf width={30} height={30} />
        </IconContainer>
        <TextAnswer>{answer.text}</TextAnswer>
      </AnswerContainer>
    ))}
  </AnswersContainer>
);

export default TextAnswers;

TextAnswers.propTypes = {
  answerOptions: PropTypes.array.isRequired,
  onAnswerClick: PropTypes.func.isRequired,
};
