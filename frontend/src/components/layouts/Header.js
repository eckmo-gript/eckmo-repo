import React from 'react';

import { Navbar, Nav } from 'react-bootstrap';

import ThemeSwitch from './ThemeSwitch';

function Header() {
    return (
        <>
            <Navbar expand="lg">
                <Navbar.Brand href="#home">ECKMO</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="https://github.com/eckmo-gript/eckmo-repo">Repository</Nav.Link>
                        <Nav.Link href="https://github.com/eckmo-gript/eckmo-repo/blob/master/README.md">Documentation</Nav.Link>
                    </Nav>

                    <Nav className="navbar-right">
                        <ThemeSwitch />
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>
    )
}

export default Header;