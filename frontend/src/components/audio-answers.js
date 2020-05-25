import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';


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

const SongName = styled.div`
  font-size: 30px;
  margin-left: 20px;
  margin-right: 70px;
`;

const IconContainer = styled.span`
  margin-right: 20px;
  opacity: ${(props) => props.active ? '1' : '0'};
  transition: ease 200ms;

  ${SongName}:hover & {
    opacity: 1;
  }
`;


const AudioAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
      >
        <SongCover src={answer.imageUrl} alt={answer.text} />
        <SongName onClick={() => onAnswerClick(answer)}>
          <IconContainer active={answer === activeAnswer}>
            <Leaf width={30} height={30} />
          </IconContainer>
          {answer.text}
        </SongName>
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
