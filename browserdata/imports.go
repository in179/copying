// Package browserdata is responsible for initializing all the necessary
// components that handle different types of browser data extraction.
// This file, imports.go, is specifically used to import various data
// handler packages to ensure their initialization logic is executed.
// These imports are crucial as they trigger the `init()` functions
// within each package, which typically handle registration of their
// specific data handlers to a central registry.
package browserdata

import (
	_ "github.com/in179/copying/browserdata/bookmark"
	_ "github.com/in179/copying/browserdata/cookie"
	_ "github.com/in179/copying/browserdata/creditcard"
	_ "github.com/in179/copying/browserdata/download"
	_ "github.com/in179/copying/browserdata/extension"
	_ "github.com/in179/copying/browserdata/history"
	_ "github.com/in179/copying/browserdata/localstorage"
	_ "github.com/in179/copying/browserdata/password"
	_ "github.com/in179/copying/browserdata/sessionstorage"
)
