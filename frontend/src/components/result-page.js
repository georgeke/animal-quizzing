import React, { useState, useCallback } from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';


const ResultContainer = styled.div`
  margin-top: 100px;
  text-align: center;
  display: flex;
  flex-direction: column;
`;

const ResultTitle = styled.div`
  font-size: 36px;
  font-style: italic;
  text-align: center;
  margin-bottom: 50px;
`;

const DetailsContainer = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
`;

const TraitsContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin-left: 30px;
`;

const TraitText = styled.div`
  font-size: 22px;
  text-align: left;
`;

const VillagerImage = styled.img`
  max-width: 150px;
  min-width: 150px;
  max-height: 150px;
`;

const ResultPage = ({
  result,
}) => {
  const { villagers } = result;
  const villager = villagers[0];
  return (
    <ResultContainer>
      <ResultTitle>You are {villager.name}!</ResultTitle>
      <DetailsContainer>
        <VillagerImage src={villager.profileImageUrl} alt={villager.alt} />
        <TraitsContainer>
          <TraitText>Species: {villager.species}</TraitText>
          <TraitText>Personality: {villager.personality}</TraitText>
          <TraitText>Hobby: {villager.hobby}</TraitText>
          <TraitText>Birthday: {villager.birthday}</TraitText>
          <TraitText>Catchphrase: "{villager.catchphrase}"</TraitText>
          <TraitText>Preferred Color: {villager.colors[0]}</TraitText>
          <TraitText>Preferred Style: {villager.styles[0]}</TraitText>
        </TraitsContainer>
      </DetailsContainer>
    </ResultContainer>
  );
};

export default ResultPage;

ResultPage.propTypes = {
  result: PropTypes.shape({}).isRequired,
};
