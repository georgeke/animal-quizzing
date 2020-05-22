import PropTypes from 'prop-types';
import styled from '@emotion/styled';
import { css } from '@emotion/core';

import theme from '../theme';

const Button = styled.button`
  background: transparent;
  border: 1px ${theme.colors.gray[4]} solid;
  border-radius: 3px;
  appearance: none;

  position: relative;
  padding-left: 32px;
  padding-right: 32px;
  height: 50px;

  color: ${theme.colors.gray[9]};
  font-size: 21px;
  font-family: 'IBM Plex Mono';
  line-height: 43px;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
  user-select: none;
  cursor: pointer;

  &:focus {
    outline: none;
  }

  display: inline-flex;
  justify-content: center;
  align-items: center;

  background: ${theme.colors.green.tea};

  &:hover {
    border-color: none;
    background: ${theme.colors.green.teaDark};
  }

  transition: color 200ms ease, background 200ms ease, border 200ms ease;

  ${(props) => props.primary && css`
    color: ${theme.colors.black};
    border: none;
    background: ${theme.colors.green.green};
    font-weight: 500;

    &:hover {
      border-color: none;
      background: ${theme.colors.green.leaf};
    }
  `}
`;

export default Button;

Button.propTypes = {
  primary: PropTypes.bool,
};