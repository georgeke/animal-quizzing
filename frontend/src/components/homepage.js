import React from 'react';
import styled from '@emotion/styled';

import { ReactComponent as Leaf } from '../assets/icons/leaf.svg';
import Button from './button';

const Title = styled.div`
  font-size: 55px;
  font-weight: 400;
  font-style: italic;
  margin-top: 60px;
  margin-bottom: 20px;
`;

const SubTitle = styled.div`
  font-size: 23px;
  margin-bottom: 60px;
`;

const HomepageContainer = styled.div`
  text-align: center;
  margin-top: 200px;
`;

const HomepageLayout = styled.div`
  max-width: 960px;
  min-width: 720px;
  margin-right: auto;
  margin-left: auto;
`;

const Homepage = () => (
  <HomepageLayout>
    <HomepageContainer>
      <Leaf width={260} height={260} />
      <Title>Which villager are you?</Title>
      <SubTitle>Animal Crossing: New Horizons</SubTitle>
      <Button>Start</Button>
    </HomepageContainer>
  </HomepageLayout>
);

export default Homepage;
