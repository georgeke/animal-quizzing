import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';


const AnswersContainer = styled.div`
  margin-top: 60px;
`;

const AnswerContainer = styled.a`
  cursor: pointer;
  margin-top: 40px;
  display: flex;
  align-items: center;
  background: white;
  border: 1px #E462B0 solid;
  border-radius: 3px;
  padding: 25px;
`;

const TextAnswer = styled.span`
  font-size: 20px;
  margin-left: 20px;
`;

const IconContainer = styled.div`
  opacity: ${(props) => props.active ? '1' : '0'};
  transition: ease 200ms;

  ${AnswerContainer}:hover & {
    opacity: 1;
  }
`;


const TextAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.text}
        onClick={() => onAnswerClick(answer)}
      >
        <IconContainer active={answer === activeAnswer}>
          <Leaf width={25} height={25} />
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
  activeAnswer: PropTypes.shape({}),
};

TextAnswers.defaultProps = {
  activeAnswer: null,
};
