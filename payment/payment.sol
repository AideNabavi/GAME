
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";



contract GameClubPayments {

    using SafeERC20 for IERC20;

    address public owner;
    uint public ID;
    event show(uint);

    event PaymentReceived(
        address indexed payer,
        address indexed token,
        uint256 amount,
        uint256 id
    );

    
    event NativePaymentReceived(
        address indexed payer,
        uint256 amount,
        uint256 paymentId
    );
    event NativePaymentReceived(
        address indexed payer,
        uint256 amount,
        uint256 packageId
    );
    mapping(address => bool) public allowedTokens;
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    event OwnershipChanged(
        address indexed oldOwner,
        address indexed newOwner
    );
    constructor() {
        owner = msg.sender;
        ID=0;
    }

    // ERC20 payment
    function payToken(
        address token,
        uint256 amount
    ) external {
        ID = ID + 1; 
        require(token != address(0), "Invalid token");
        require(amount > 0, "Invalid amount");
        require(
            allowedTokens[token],
            "Token not supported"
        );
        IERC20(token).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        emit PaymentReceived(
            msg.sender,
            token,
            amount,
            ID
        );
    }

    // Native coin payment
    function payNative(
        uint256 packageId
    ) external payable {

        require(msg.value > 0, "No payment");

        emit NativePaymentReceived(
            msg.sender,
            msg.value,
            packageId
        );
    }

    // Withdraw ERC20
    function withdrawToken(
        address token,
        uint256 amount,
        address to
    ) external onlyOwner {

        IERC20(token).safeTransfer(to, amount);
    }

    // Withdraw native coin
    function withdrawNative(
        uint256 amount,
        address payable to
    ) external onlyOwner {

        require(address(this).balance >= amount, "Insufficient balance");

        to.transfer(amount);
    }


    function setToken(
    address token,
    bool allowed
    ) external onlyOwner {
        allowedTokens[token] = allowed;
    }

    //این تابع برای  دیده مقدار توکن هایی است که در قرار است 
    function getTokenBalance(
        address token
    ) external view returns (uint256) {

        return IERC20(token).balanceOf(address(this));
    }

    // برای تغییر اونر 
    function changeOwner(
        address newOwner
    ) external onlyOwner {

        require(newOwner != address(0), "Invalid owner");

        address oldOwner = owner;

        owner = newOwner;

        emit OwnershipChanged(
            oldOwner,
            newOwner
        );
    }



    receive() external payable {
        require(msg.value > 0, "No payment");

        ID++;

        emit NativePaymentReceived(
            msg.sender,
            msg.value,
            ID
        );
    }
}