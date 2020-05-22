import React from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';

import TextAnswers from './text-answers';


const QuestionContainer = styled.div`
  margin-top: 100px;
  text-align: center;
`;

const QuestionText = styled.div`
  font-size: 36px;
  font-style: italic;
`;

const QuestionPage = ({ question }) => {
  const { questionType, questionText, answers } = question;

  let answersComponent;
  if (questionType === 'text') {
    answersComponent = <TextAnswers answers={answers} />;
  }

  return (
    <QuestionContainer>
      <QuestionText>
        {questionText}
      </QuestionText>
      {answersComponent}
    </QuestionContainer>
  );
};

export default QuestionPage;

QuestionPage.propTypes = {
  question: PropTypes.shape({}).isRequired,
};
