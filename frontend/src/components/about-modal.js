import React from 'react';
import styled from 'styled-components';

import { ReactComponent as Kat } from '../assets/icons/kat.svg';
import { ReactComponent as George } from '../assets/icons/george.svg';


export const Overlay = styled.span`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background: rgba(0, 0, 0, 0.7);
`;

const ModalContainer = styled.span`
  text-align: center;
  z-index: 2;
  border-radius: 3px;
  background-color: #ffeded;
  justify-content: center;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  padding: 50px;
  padding-bottom: 20px;
`;

const Text = styled.div`
  font-style: italic;
  color: #E462B0;
  margin-bottom: 30px;
`;

const Name = styled.div`
  font-style: italic;
  font-size: 22px;
  color: #E462B0;
  font-weight: bold;
  margin-right: 20px;
  margin-left: 20px;
`;

const And = styled.div`
  color: #E462B0;
`;

const NameContainer = styled.div`
  display: flex;
  margin-bottom: 20px;
  align-items: center;
`;

const AvatarContainer = styled.div`
  display: flex;
  justify-content: center;
`;

const Avatar = styled.div`
  margin-left: 10px;
  margin-right: 10px;
`;

const Close = styled.div`
  cursor: pointer;
  margin-top: 50px;
  font-size: 12px;
  text-decoration: underline;
`;


const AboutModal = ({ closeModal }) => (
  <>
    <Overlay onClick={closeModal} />
    <ModalContainer>
      <Text>Made by</Text>
      <NameContainer>
        <Name>George</Name>
        <And>+</And>
        <Name>Kat</Name>
      </NameContainer>
      <AvatarContainer>
        <Avatar>
          <George />
        </Avatar>
        <Avatar>
          <Kat />
        </Avatar>
      </AvatarContainer>
      <Close onClick={closeModal}>Close</Close>
    </ModalContainer>
  </>
);

export default AboutModal;
