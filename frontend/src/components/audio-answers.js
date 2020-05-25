import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';


const AnswersContainer = styled.div`
  margin-top: 60px;
  margin-bottom: 120px;
  display: flex;
  justify-content: center;
`;

const AnswerContainer = styled.a`
  cursor: pointer;
  margin-top: 40px;
  margin-left: 40px;
  margin-right: 40px;
  align-items: center;
  display: flex;
  flex-direction: column;
`;

const SongCover = styled.img`
  max-width: 300px;
  margin-bottom: 20px
`;

const SongName = styled.span`
  font-size: 30px;
  margin-left: 20px;
`;


const AudioAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
      >
        <SongCover src={answer.imageUrl} alt={answer.text} />
        <SongName onClick={() => onAnswerClick(answer)}>{answer.text}</SongName>
      </AnswerContainer>
    ))}
  </AnswersContainer>
);

export default AudioAnswers;

AudioAnswers.propTypes = {
  answerOptions: PropTypes.array.isRequired,
  onAnswerClick: PropTypes.func.isRequired,
  activeAnswer: PropTypes.shape({}).isRequired,
};
