# MWORKS Login / License Recovery Confirmed

Timestamp: 2026-07-09 CST

Scope: UGV M6 runtime recovery only. This note records the recovery path for
MWORKS/Sysplorer login and license activation. It does not claim four-track
completion, controller success, final score, or submission readiness.

## What Happened

The earlier runtime API probe failed with:

```text
L5104-B0
软件尚未激活，请前往菜单栏“帮助”>“使用许可”窗口激活软件后重试
```

The GUI also displayed `登录失败，请检查网络后重试` in the license dialog. This
must not be treated as a network blocker by default. The successful recovery was
to operate the real visible Sysplorer UI:

1. Reopen/restore the real `Sysplorer` window.
2. Open `帮助 -> 使用许可`.
3. Click the real `登录` button when the license dialog shows `账号：未登录`.
4. Use `账号密码登录`, fill the approved in-memory account credentials, and
   click the real `登 录` button.
5. Confirm the Sysplorer title changes to `Sysplorer [教育版]`.
6. Confirm license activation through `帮助 -> 使用许可` when needed.
7. Verify with a 1 s API simulation probe.

No credential value is stored in this note.

## Verification

Successful verification evidence:

```text
Results/simulations/license_gui_confirm_1s_20260709_after_real_login/
```

Key probe results:

```text
open_dependency_model_file: ok
open_model_file: ok
open_model: ok
check_model: ok
simulate_model: ok
simulation_exit_state: 0
simulation_state: Idle
score variables: T, cR, cO, P
T=1.0, cR=0.0, cO=0.0, P=10.0
```

The probe target was:

```text
UGV.Test.Saidao2Eval
stopTime=1
controller_version=controller_v5_bounded_linear_deployability
```

## Future Handling

If `L5104-B0` or the license dialog reappears, follow
`Docs/Workflows/mworks_ugv_simulation_workflow.md` before declaring a blocker:
click the real login button, use the approved in-memory credentials, activate
through `帮助 -> 使用许可`, then prove recovery with the same 1 s API probe.

Do not store credentials in repo files, logs, evidence, or email. Stop only for
unknown modals, CAPTCHA/MFA, repeated credential rejection after the real login
flow, or broad runtime changes outside this recovery path.
