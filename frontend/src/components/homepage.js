import React from 'react';
import styled from '@emotion/styled';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';
import Button from './button';

const Title = styled.div`
  font-size: 55px;
  font-weight: 400;
  font-style: italic;
  margin-top: 85px;
  margin-bottom: 20px;
`;

const SubTitle = styled.div`
  font-size: 24px;
  margin-bottom: 55px;
`;

const HomepageContainer = styled.div`
  text-align: center;
  margin-top: 200px;
`;

const Homepage = () => (
  <HomepageContainer>
    <Leaf width={270} height={270} />
    <Title>Which villager are you?</Title>
    <SubTitle>Animal Crossing: New Horizons</SubTitle>
    <Button primary>Start</Button>
  </HomepageContainer>
);

export default Homepage;
