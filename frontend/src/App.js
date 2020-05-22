import React, { useState } from 'react';
import styled from '@emotion/styled';

import Homepage from './components/homepage';
import QuestionPage from './components/question-page';

const AppContainer = styled.div`
  max-width: 960px;
  min-width: 720px;
  margin-right: auto;
  margin-left: auto;
`;

const App = () => {
  const [answers, setAnswers] = useState(null);
  const [question, setQuestion] = useState(null);

  let component;

  if (question && answers) {
    component = <QuestionPage question={question} />
  } else {
    component = (
      <Homepage
        setAnswers={setAnswers}
        setQuestion={setQuestion}
      />
    );
  }

  return (
    <AppContainer>
      {component}
    </AppContainer>
  );
};

export default App;
