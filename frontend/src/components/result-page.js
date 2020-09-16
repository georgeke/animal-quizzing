import React, { useState } from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';

import AboutModal from './about-modal';


const ResultContainer = styled.div`
  margin-top: 130px;
  text-align: center;
  margin-bottom: 100px;
`;

const ResultTitle = styled.div`
  font-size: 36px;
  font-style: italic;
  text-align: center;
  margin-bottom: 70px;
`;

const Name = styled.span`
  font-weight: bold;
`;

const TraitsContainer = styled.div`
  font-size: 22px;
  text-align: left;
  display: flex;
  justify-content: space-evenly;
  margin-bottom: 100px;
`;

const TraitColumn = styled.div`
  display: flex;
`;

const Trait = styled.div`
  letter-spacing: 0.125rem;
  font-size: 17px;
  margin-bottom: 30px;
`;

const TraitText = styled.div`
  letter-spacing: 0;
  font-size: 22px;
  font-style: italic;
  margin-left: 45px;
  margin-bottom: 21px;
`;

const MoreLink = styled.a`
  color: black;
`;

const VillagerImage = styled.img`
  max-width: 150px;
  min-width: 150px;
  max-height: 150px;
  margin-bottom: 50px;
`;

const Link = styled.a`
  font-size: 16px;
  font-style: italic;
  color: #E462B0;
  text-decoration: underline;
  cursor: pointer;
`;


const ResultPage = ({
  result,
}) => {
  const { villagers } = result;
  const villager = villagers[0];

  const [modalOpen, setModalOpen] = useState(false);

  return (
    <ResultContainer>
      <ResultTitle>{'You are '}
        <Name>{villager.name}</Name>!
      </ResultTitle>
      <VillagerImage src={villager.profileImageUrl} alt={villager.alt} />
      <TraitsContainer>
        <TraitColumn>
          <div>
            <Trait>Species:</Trait>
            <Trait>Birthday:</Trait>
            <Trait>Favourite Colour:</Trait>
            <Trait>Favourite Style:</Trait>
          </div>
          <div>
            <TraitText>{villager.species}</TraitText>
            <TraitText>{villager.birthday}</TraitText>
            <TraitText>{villager.colors[0]}</TraitText>
            <TraitText>{villager.styles[0]}</TraitText>
          </div>
        </TraitColumn>
        <TraitColumn>
          <div>
            <Trait>Personality:</Trait>
            <Trait>Catchphrase:</Trait>
            <Trait>Hobby:</Trait>
            <Trait>
              <MoreLink target="_blank" href={`https://animalcrossing.fandom.com/wiki/${villager.name}`}>
                See more &#8674;
              </MoreLink>
            </Trait>
          </div>
          <div>
            <TraitText>{villager.personality}</TraitText>
            <TraitText>"{villager.catchphrase}"</TraitText>
            <TraitText>{villager.hobby}</TraitText>
          </div>
        </TraitColumn>
      </TraitsContainer>
      <Link onClick={() => setModalOpen(true)}>
        Made with &#10084; in Quarantine
      </Link>
      {modalOpen && <AboutModal closeModal={() => setModalOpen(false)} />}
    </ResultContainer>
  );
};

export default ResultPage;

ResultPage.propTypes = {
  result: PropTypes.shape({}).isRequired,
};
