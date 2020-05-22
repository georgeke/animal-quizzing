import React from 'react';
import styled from '@emotion/styled';

import Homepage from './components/homepage';
import QuestionPage from './components/question-page';

const AppContainer = styled.div`
  max-width: 960px;
  min-width: 720px;
  margin-right: auto;
  margin-left: auto;
`;

const App = () => (
  <AppContainer>
    <Homepage />
  </AppContainer>
);

export default App;
