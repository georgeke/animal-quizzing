import React, { useState } from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';
import axios from 'axios';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';
import Button from './button';

const Title = styled.div`
  font-size: 55px;
  font-weight: 400;
  font-style: italic;
  margin-top: 85px;
  margin-bottom: 30px;
`;

const SubTitle = styled.div`
  font-size: 24px;
  margin-bottom: 55px;
`;

const HomepageContainer = styled.div`
  text-align: center;
  margin-top: 200px;
`;

const Homepage = ({ setAnswers, setQuestion }) => {
  const [isLoading, setIsLoading] = useState(false);

  const onStartClick = () => {
    setIsLoading(true);
    // TODO: replace with actual url
    axios.post('https://animal-quizzing.herokuapp.com/question', {
      answers: [],
    })
    .then((response) => {
      setIsLoading(false);

      const { data } = response;

      setAnswers(data.answers);
      setQuestion(data.nextQuestion);
    })
    .catch((error) => {
      setIsLoading(false);
      console.log(error);
    });
  };

  return (
    <HomepageContainer>
      <Leaf width={270} height={270} />
      <Title>Which villager are you?</Title>
      <SubTitle>Animal Crossing: New Horizons</SubTitle>
      <Button onClick={onStartClick} disabled={isLoading}>{isLoading ? 'Starting' : 'Start'}</Button>
    </HomepageContainer>
  );
}

export default Homepage;

Homepage.propTypes = {
  setAnswers: PropTypes.func.isRequired,
  setQuestion: PropTypes.func.isRequired,
}
