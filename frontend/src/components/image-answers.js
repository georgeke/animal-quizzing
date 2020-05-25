import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';


const AnswersContainer = styled.div`
  margin-top: 60px;
  margin-bottom: 120px;
  display: flex;
  justify-content: space-around;
`;

const AnswerContainer = styled.a`
  cursor: pointer;
  margin-top: 40px;
  align-items: center;
`;

const ImageAnswer = styled.span`
  font-size: 20px;
  margin-left: 20px;
  max-width: 100px;
`;


const ImageAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
        onClick={() => onAnswerClick(answer)}
      >
        <ImageAnswer><img src={answer.imageUrl} alt={answer.text} /></ImageAnswer>
      </AnswerContainer>
    ))}
  </AnswersContainer>
);

export default ImageAnswers;

ImageAnswers.propTypes = {
  answerOptions: PropTypes.array.isRequired,
  onAnswerClick: PropTypes.func.isRequired,
  activeAnswer: PropTypes.shape({}).isRequired,
};
