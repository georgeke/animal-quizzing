import { ReactComponent as Leaf } from "../assets/icons/leaf.svg";
import PropTypes from "prop-types";
import React from "react";
import styled from "styled-components";

const AnswersContainer = styled.div`
  margin-top: 60px;
  margin-bottom: 120px;
  display: flex;
  justify-content: space-around;
`;

const AnswerContainer = styled.a`
  cursor: pointer;
  margin-top: 40px;
  align-items: center;
  background: white;
  border-radius: 0.75em;
  display: flex;
`;

const ImageAnswer = styled.img`
  max-width: 100px;
  padding: 40px;
  padding-left: 10px;
`;

const IconContainer = styled.div`
  opacity: ${(props) => (props.active ? "1" : "0")};
  transition: ease 200ms;
  align-self: flex-start;
  margin: 5px;

  ${AnswerContainer}:hover & {
    opacity: 1;
  }
`;

const ImageAnswers = ({ answerOptions, onAnswerClick, activeAnswer }) => (
  <AnswersContainer>
    {answerOptions.map((answer) => (
      <AnswerContainer
        key={answer.imageUrl}
        onClick={() => onAnswerClick(answer)}
      >
        <IconContainer active={answer === activeAnswer}>
          <Leaf width={25} height={25} />
        </IconContainer>
        <ImageAnswer src={answer.imageUrl} alt={answer.text} />
      </AnswerContainer>
    ))}
  </AnswersContainer>
);

export default ImageAnswers;

ImageAnswers.propTypes = {
  answerOptions: PropTypes.array.isRequired,
  onAnswerClick: PropTypes.func.isRequired,
  activeAnswer: PropTypes.shape({}),
};

ImageAnswers.defaultProps = {
  activeAnswer: null,
};
