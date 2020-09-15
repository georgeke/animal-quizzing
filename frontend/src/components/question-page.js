import React, { useState, useCallback } from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';
import axios from 'axios';

import AudioAnswers from './audio-answers';
import ImageAnswers from './image-answers';
import TextAnswers from './text-answers';
import Button from './button';


const QuestionContainer = styled.div`
  margin-top: 100px;
  text-align: center;
`;

const QuestionText = styled.div`
  font-size: 36px;
  font-style: italic;
  text-align: center;
`;

const ButtonContainer = styled.div`
  margin-top: 63px;
`;

const QuestionPage = ({
  question,
  currentAnswers,
  setAnswers,
  setQuestion,
  setResult,
}) => {
  const {
    questionId,
    questionFormat,
    questionText,
    villagerTrait,
    answers
  } = question;
  const [activeAnswer, setActiveAnswer] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const buttonDisabled = activeAnswer === null || isLoading;

  const onNext = useCallback(() => {
    const newAnswer = {
      questionId,
      questionText,
      questionFormat,
      villagerTrait,
      answer: activeAnswer,
    };

    const newAnswers = currentAnswers;
    newAnswers.push(newAnswer);

    setIsLoading(true);

    // TODO: replace with actual url
    axios.post('https://animal-quizzing.herokuapp.com/question', {
      answers: newAnswers,
    })
    .then((response) => {
      setIsLoading(false);

      const { data } = response;

      if (data.answers && data.nextQuestion) {
        setAnswers(data.answers);
        setQuestion(data.nextQuestion);
      } else if (data.villagers) {
        setResult(data)
      }
      setActiveAnswer(null);
    })
    .catch((error) => {
      setIsLoading(false);
      console.log(error);
    });
  }, [
    setResult,
    activeAnswer,
    currentAnswers,
    setAnswers,
    setQuestion,
    questionId,
    questionText,
    questionFormat,
    villagerTrait,
  ]);
  let answersComponent;
  if (questionFormat === 'text') {
    answersComponent = (
      <TextAnswers
        answerOptions={answers}
        onAnswerClick={setActiveAnswer}
        activeAnswer={activeAnswer}
      />
    );
  } else if (questionFormat === 'image') {
    answersComponent = (
      <ImageAnswers
        answerOptions={answers}
        onAnswerClick={setActiveAnswer}
        activeAnswer={activeAnswer}
      />
    );
  } else if (questionFormat === 'audio') {
    answersComponent = (
      <AudioAnswers
        answerOptions={answers}
        onAnswerClick={setActiveAnswer}
        activeAnswer={activeAnswer}
      />
    );
  }

  return (
    <QuestionContainer>
      <QuestionText>
        {questionText}
      </QuestionText>
      {answersComponent}
      <ButtonContainer>
        <Button disabled={buttonDisabled} onClick={onNext}>{isLoading ? '...' : 'Next'}</Button>
      </ButtonContainer>
    </QuestionContainer>
  );
};

export default QuestionPage;

QuestionPage.propTypes = {
  question: PropTypes.shape({}).isRequired,
  currentAnswers: PropTypes.array.isRequired,
  setAnswers: PropTypes.func.isRequired,
  setQuestion: PropTypes.func.isRequired,
};
