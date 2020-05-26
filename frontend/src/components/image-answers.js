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

const ImageAnswer = styled.img`
  margin-left: 10px;
  max-width: 100px;
`;


const ImageAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
        onClick={() => onAnswerClick(answer)}
      >
        <ImageAnswer src={answer.imageUrl} alt={answer.text} />
      </AnswerContainer>
    ))}
  </AnswersContainer>
);

export default ImageAnswers;

ImageAnswers.propTypes = {
  answerOptions: PropTypes.array.isRequired,
  onAnswerClick: PropTypes.func.isRequired,
  activeAnswer: PropTypes.shape({}),
};

ImageAnswers.defaultProps = {
  activeAnswer: null,
};
