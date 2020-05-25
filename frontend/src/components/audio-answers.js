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

const AudioAnswer = styled.span`
  font-size: 20px;
  margin-left: 20px;
`;

const SongCover = styled.img`
  max-width: 200px;
`;

const SongName = styled.span`
  font-size: 20px;
  margin-left: 20px;
`;


const AudioAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
      >
        <AudioAnswer>
          <SongCover src={answer.imageUrl} alt={answer.text} />
          <SongName onClick={() => onAnswerClick(answer)}>{answer.text}</SongName>
        </AudioAnswer>
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
