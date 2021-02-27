import React, { useState } from "react";

import Button from "./button";
import { ReactComponent as Leaf } from "../assets/icons/leaf.svg";
import PropTypes from "prop-types";
import axios from "axios";
import styled from "@emotion/styled";

const Title = styled.div`
  font-size: 65px;
  font-weight: 400;
  margin-top: 85px;
  margin-bottom: 22px;
`;

const SubTitle = styled.div`
  font-size: 23px;
  margin-bottom: 60px;
  font-style: italic;
`;

const HomepageContainer = styled.div`
  text-align: center;
  margin-top: 190px;
`;

const Homepage = ({ setAnswers, setQuestion }) => {
  const [isLoading, setIsLoading] = useState(false);

  const onStartClick = () => {
    setIsLoading(true);
    // TODO: replace with actual url
    axios
      .post("https://localhost:5000/question", {
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
      {/* <Button onClick={onStartClick} disabled={isLoading}>
        {isLoading ? "Starting" : "Start"}
      </Button> */}

      <button onClick={onStartClick} disabled={isLoading} className="button">
        {isLoading ? "Starting" : "Start"}
      </button>
    </HomepageContainer>
  );
};

export default Homepage;

Homepage.propTypes = {
  setAnswers: PropTypes.func.isRequired,
  setQuestion: PropTypes.func.isRequired,
};
